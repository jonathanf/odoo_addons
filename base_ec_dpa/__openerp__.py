# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014-Today Jonathan Finlay <jfinlay@riseup.net>.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "DPA Ecuador - División Pólítico Administrativa",
    "version": "1.0",
    "description": """
DPA Ecuador - División Pólítico Administrativa
==============================================
Add to Odoo the INEC (Instituto Nacional de Estadísticas y Cesos - Ecuador) databases for State, Cities and Parish

Provides:
---------
    * Partner view with new field order: country, state, city
    * Add parish model
    * Admin views for the model city and parish.
    * Domain validation for DPA models

Source of data: http://www.inec.gob.ec
    """,
    "shortdesc": "Base EC DPA",
    "author": "Jonathan Finlay <jfinlay@riseup.net>",
    "website": "https://github.com/jonathanf",
    "category": "Localization",
    "sequence": 1,
    "complexity": "easy",
    "depends": [
        'base',
        ],
    "data": [
        'data/res.country.state.csv',
        'data/res.country.city.csv',
        'data/res.country.parish.csv',
        'security/ir.model.access.csv'
    ],
    "init_xml": [],
    "demo_xml": [],
    "update_xml": [
        'view/res_country_view.xml',
        'view/res_company_view.xml',
        'view/res_partner_view.xml',
    ],
    "active": False,
    "installable": True,
    "certificate": "",
}
