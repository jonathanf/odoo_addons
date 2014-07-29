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

from openerp.osv import osv

class res_partner(osv.osv):
    """Base EC Model-tools for localization"""
    _name = "res.partner"
    _inherit = "res.partner"

    def check_doc_ec(self, cr, uid, id, ref, context=None):
        if ref:
            base_ec_obj = self.pool.get("base.ec")
            if not base_ec_obj.check_doc_ec(ref):
                return {
                    'value': {
                        'ref': ''
                    },
                    'warning': {
                        'title': 'User error',
                        'message': 'The document is not valid'
                    }
                }
        return {}

res_partner()
