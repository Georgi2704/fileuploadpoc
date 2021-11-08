# Copyright 2019-2020 SURF.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from http import HTTPStatus
from typing import List
from uuid import UUID

from fastapi import HTTPException
from fastapi.param_functions import Body, Depends
from fastapi.routing import APIRouter
from starlette.responses import Response

from server.api import deps
from server.api.deps import common_parameters
from server.api.error_handling import raise_status
from server.crud import map_crud
from server.db.models import MapsTable, UsersTable
from server.schemas import Map, MapCreate, MapCreateAdmin, MapUpdate, MapUpdateAdmin

router = APIRouter()


@router.get("/")
def get_hello(response: Response) -> str:
    return "Hello Formatics!"
