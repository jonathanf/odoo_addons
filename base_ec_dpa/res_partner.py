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

from openerp.osv import fields, osv

ADDRESS_FIELDS = ('street', 'street2', 'zip', 'city', 'state_id', 'country_id', 'parish_id')


class res_partner(osv.osv):
    _name = "res.partner"
    _inherit = "res.partner"

    def _address_fields(self, cr, uid, context=None):
        """ Returns the list of address fields that are synced from the parent
        when the `use_parent_address` flag is set. """
        return list(ADDRESS_FIELDS)

    _columns = {
        'country_id': fields.many2one('res.country', 'Country'),
        'state_id': fields.many2one("res.country.state", 'State', domain="[('country_id','=',country_id)]"),
        'city': fields.many2one('res.country.city', 'City', domain="[('state_id','=',state_id)]"),
        'parish_id': fields.many2one('res.country.parish', 'Parish', domain="[('city_id','=',city)]")
    }

res_partner()