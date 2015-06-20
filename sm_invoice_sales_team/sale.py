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

class sale_order(osv.osv):
    _inherit = "sale.order"

    def _prepare_invoice(self, cr, uid, order, lines, context=None):
        if context is None:
            context = {}
        invoice_vals = super(sale_order, self)._prepare_invoice(cr, uid, order, lines, context=context)
        invoice_vals.update({'section_id':order.section_id and order.section_id.id or False })
        return invoice_vals
        
sale_order()
