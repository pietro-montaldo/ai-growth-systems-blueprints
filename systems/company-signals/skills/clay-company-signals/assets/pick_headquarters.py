"""Clay code step "Pick headquarters" for the clay-company-signals skill.

Used in the "Signals: add to watchlist" workflow, between "Enrich company" and
"Add company to watchlist". Picks the headquarters city, state and address from the
Enrich Company location lists, so the company record gets them.

Inputs to wire on the node (sourceNodeId = the "Enrich company" node):
  structured_locations   $.result.structured_locations
  locations              $.result.locations
  locality               $.result.locality

Outputs: hq_city, hq_state, hq_address (text, empty when Clay has nothing).
"""


def text(value):
    return "" if value is None else str(value).strip()


def first(items, flag):
    """The entry marked with flag, else the first entry, else {}."""
    items = [i for i in (items or []) if isinstance(i, dict)]
    return next((i for i in items if i.get(flag)), items[0] if items else {})


def handler(context):
    hq = first(context.get_input("structured_locations"), "is_headquarters")
    primary = first(context.get_input("locations"), "is_primary")
    inferred = primary.get("inferred_location") or {}
    return {
        "hq_city": text(hq.get("city") or inferred.get("locality")),
        "hq_state": text(hq.get("state") or inferred.get("admin_district")),
        "hq_address": text(inferred.get("formatted_address") or primary.get("address")
                           or context.get_input("locality")),
    }
