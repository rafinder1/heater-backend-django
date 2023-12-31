﻿# HEATER BACKEND

[![Build Status](https://github.com/rafinder1/heater-backend-django/actions/workflows/django.yml/badge.svg)](https://github.com/rafinder1/heater-backend-django/actions/workflows/django.yml) 

The Heater Backend project has been developed as part of a master's thesis in sustainable construction at the Military University of Technology in Warsaw.

The HEATER BACKEND application provides a range of endpoints allowing access to various information and functionalities related to construction projects. Individual endpoints, such as `materials`, `type_layers`, `thermal_isolation`, `isolation`, `wall`, and `plaster`, enable detailed retrieval of information about available construction materials, types of construction layers, thermal insulation, building insulation, wall types, and plaster varieties. Currently, these endpoints predominantly utilize the GET method to deliver diverse information about construction materials to users.

In planned future versions of the application, there is an intention to introduce functionality enabling users to add their own materials. Currently, data for several dozen materials has been imported into the database from an Excel file. Additional endpoints, such as `materials/filter` and `thickness_material/filter`, allow the filtering of materials based on specific categories, enhancing flexibility in accessing information.

Furthermore, the `calculate`, `multi_variant_calc`, and `calculate_amount_polys_price` endpoints handle various calculations based on provided parameters. These methods leverage a library available at https://github.com/rafinder1/temperature-calculator, ensuring precise and effective temperature-related calculations within the context of construction projects.
