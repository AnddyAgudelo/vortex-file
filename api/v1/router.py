from api.v1.files.files_controller import files_router
from utils.helpers import set_prefix

routers_v1 = [
    files_router,
]

set_prefix(routers_v1, "/v1")
