from beet import Context
from simple_item_plugin import NAMESPACE



def beet_default(ctx: Context):
    NAMESPACE.set(ctx.project_id)
    print("Hello, world!")

