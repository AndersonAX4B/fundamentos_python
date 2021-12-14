from odoo import models, fields, api
from odoo.tools.translate import _
from datetime import datetime


class MinhaClasse(models.Model):
    _name = 'purchase.minha.classe'
    _description = 'Requisition Product'

    priority = fields.Selection([('0', 'Normal'), ('1', 'Urgent')], 'Priority', default='0', index=True)
    name = fields.Char(string='Product')
    currency_id = fields.Many2one('res.currency', 'Currency', store=True)

    purchase_requisition_id = fields.Many2one('ax4b_purchase.purchase_requisition', string='Purchase Requisition')
    id_reserve_note = fields.Integer(related='purchase_requisition_id.id_reserve_note',
                                     string='Requisition Reservation Note ID')

    product_id = fields.Many2one('product.product', string='Product Code')
    description = fields.Text(related='product_id.description', string='Description')
    expected_date = fields.Date(string='Expected Date')
    definition_of_service = fields.Selection(
        [("STOCKRETIREMENT", "Stock Retirement"), ("PURCHASINGPROCESS", "Purchasing Process")],
        string='Definition of Service')
    unit_price = fields.Float(related='product_id.list_price', string='Unit Price')
    total_value = fields.Monetary(string='Total Value')
    requester_id = fields.Many2one('res.users', string='Requester')
    situation = fields.Selection([("SDC", "SDC"), ("INPROCESS", "In Process"), ("SDCSENT", "SDC Sent"),
                                  ("CONCLUDED", "Concluded")], string="Situation", default="SDC")
    cost_center_id = fields.Many2one('ax4b_accounting.cost_center', string='Cost Center')
    cost_center_description = fields.Text(related='cost_center_id.description', string='Cost Center Description')
    buyer_group_id = fields.Many2one('purchase_requisition.grupo_comprador', string='Buyer Group')
    uom_id = fields.Many2one('uom.uom', string='Unit of Measure')

    # Budget page
    reserve_note_id = fields.Many2one('ax4b_public_budget.reserve_note', string='Reserve Note')
    process_id = fields.Many2one(related='reserve_note_id.process_id')

    @api.onchange("unit_price")
    def _calculates_total_value(self):
        for record in self:
            record['total_value'] = record.quantity * record.unit_price

    @api.onchange("product")
    def _automatic_product_name(self):
        for record in self:
            record['name'] = record.product_id.name

    def reset_reserved(self):
        if self.reserved:
            self.reserved = False

    def notify_user(self, param1, param2, param3, param4, param5, param6):
        pass
