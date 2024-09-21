from fastapi import APIRouter


def set_prefix(routers: list[APIRouter], prefix: str):
    for router in routers:
        router.prefix = prefix
