from beet import Context
from simple_item_plugin.types import NAMESPACE, Lang
from simple_item_plugin.item import Item


def beet_default(ctx: Context):
    NAMESPACE.set(ctx.project_id)
    print("Hello, world!")
    graplin = Item(
        id="graplin",
        item_name=(
            f"{NAMESPACE}.item.graplin",
            {Lang.en_us: "Graplin", Lang.fr_fr: "Graplin"},
        ),
        custom_model_data=1432006,
    )
