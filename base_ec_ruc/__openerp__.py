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
    "name": "RUC Ecuador - Validación RUC/Cédula",
    "version": "1.0",
    "description": """
RUC Ecuador - Validación RUC/Cédula
===================================
Add to Odoo the formulas to validate RUC/Cédula of Ecuador Civil Registry

Provides:
---------
    * Partner view with 'ref' field validation
    * Company view with 'ref' field validation
    * Add Formulas to validate RUC/Cédula.

Alternative you can use https://code.google.com/r/jmfinlayp-vatnumber/ to get RUC validator.

    """,
    "shortdesc": "Base EC RUC",
    "author": "Jonathan Finlay <jfinlay@riseup.net>",
    "website": "https://github.com/jonathanf",
    "category": "Localization",
    "sequence": 1,
    "complexity": "medium",
    "depends": [
        'base',
    ],
    "data": [],
    "init_xml": [],
    "demo_xml": [],
    "update_xml": [
        'view/res_company_view.xml',
        'view/res_partner_view.xml',
    ],
    "active": False,
    "installable": True,
    "certificate": "",
}
