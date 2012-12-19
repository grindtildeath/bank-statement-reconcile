# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Joel Grand-Guillaume
#    Copyright 2011-2012 Camptocamp SA
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

from openerp.osv.orm import Model
from openerp.osv import fields


class account_move(Model):
    _inherit='account.move'
    
    def unlink(self, cr, uid, ids, context=None):
        """
        Delete the reconciliation when we delete the moves. This
        allow an easier way of cancelling the bank statement.
        """
        for move in self.browse(cr, uid, ids, context=context):
            for move_line in move.line_id:
                if move_line.reconcile_id:
                    move_line.reconcile_id.unlink(context=context)
        return super(account_move, self).unlink(cr, uid, ids, context=context)
        


