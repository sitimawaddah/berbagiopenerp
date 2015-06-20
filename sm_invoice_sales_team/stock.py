# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Mentis d.o.o. (www.mentis.si/openerp)
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

from openerp.osv import fields, osv, orm
from openerp.tools.translate import _
from openerp import netsvc
from openerp import tools
from openerp.tools import float_compare, DEFAULT_SERVER_DATETIME_FORMAT
import openerp.addons.decimal_precision as dp
import logging
from dateutil.relativedelta import relativedelta
from datetime import datetime

import time
import pytz
_log = logging.getLogger(__name__)

class stock_picking(osv.osv):
    _inherit = 'stock.picking'

    def _prepare_invoice(self, cr, uid, picking, partner, inv_type, journal_id, context=None):
        if context is None:
            context = {}
        invoice_vals = super(stock_picking, self)._prepare_invoice(cr, uid, picking, partner, inv_type, journal_id, context=context)
        section_id=False
        if picking.sale_id:
            order = picking.sale_id
            section_id=order.section_id and order.section_id.id or False

        invoice_vals.update({'section_id':section_id })
        return invoice_vals

stock_picking()

