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

class base_ec(osv.osv):
    """Base EC Model-tools for localization"""
    _name = 'base.ec'
    _description = "Base EC Model-tools for localization"

    def _check_vat_ec(self, ruc):
        """
        Check Ecuador RUC number.
        """
        if len(ruc) != 13:
            return False

        result = 0
        residue = 0

        if int(ruc[2]) == 6:
            # Public RUC
            coefficient = "32765432"
            checker = int(ruc[8])
            for i in range(8):
                result += (int(ruc[i]) * int(coefficient[i]))
                residue = result % 11
            if residue == 0:
                result = residue
            else:
                result = 11 - residue
        elif int(ruc[2]) == 9:
            # Juridical RUC
            coefficient = "432765432"
            checker = int(ruc[9])
            for i in range(9):
                result += (int(ruc[i]) * int(coefficient[i]))
                residue = result % 11
            if residue == 0:
                result = residue
            else:
                result = 11 - residue
        elif int(ruc[2]) < 6:
            # Natural RUC
            coefficient = "212121212"
            checker = int(ruc[9])
            for i in range(9):
                sum = (int(ruc[i]) * int(coefficient[i]))
                if sum > 10:
                    str_sum = str(sum)
                    sum = int(str_sum[0]) + int(str_sum[1])
                result += sum
            residue = result % 10
            if residue == 0:
                result = residue
            else:
                result = 10 - residue
        else:
            return False

        if result != checker:
            return False

        return True

    def _check_identity_card_ec(self, doc):
        value = [int(doc[x]) * (2 - x % 2) for x in range(9)]
        total = sum(map(lambda x: x > 9 and x - 9 or x, value))
        if int(int(doc[9] if int(doc[9]) != 0 else 10)) != (10 - int(str(total)[-1:])):
            return False
        return True

    def check_doc_ec(self, doc):
        value = int(doc)
        if value < 0:
            raise osv.except_osv('', 'not a positive integer')

        if len(doc) == 13:
            return self._check_vat_ec(doc)
        elif len(doc) == 10:
            return self._check_identity_card_ec(doc)
        return False

base_ec()
