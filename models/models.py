# -*- coding: utf-8 -*-
from collections import defaultdict

from markupsafe import Markup

from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero, plaintext2html
import logging

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    student_name = fields.Char('Student Name', tracking=True)
    university_no = fields.Char('University number', tracking=True)
    college_name = fields.Char('College Name', tracking=True)
    department_name = fields.Char('Department Name', tracking=True)
    stage_no = fields.Char('Stage Number', tracking=True)
    study_type = fields.Char('Study Type', tracking=True)
    year_study = fields.Char('Year of Study', tracking=True)
    receipt_no = fields.Char('Receipt No.', tracking=True)
    receipt_date = fields.Char('Receipt Date', tracking=True)
    type_payment = fields.Char('Payment Type', tracking=True)
    instrument_no = fields.Char('Instrument No.', tracking=True)
    instrument_date = fields.Char('Instrument Date', tracking=True)
    account_name = fields.Char('Account Name', tracking=True)


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    student_name = fields.Char('Student Name', tracking=True)
    university_no = fields.Char('University number', tracking=True)
    college_name = fields.Char('College Name', tracking=True)
    department_name = fields.Char('Department Name', tracking=True)
    stage_no = fields.Char('Stage Number', tracking=True)
    study_type = fields.Char('Study Type', tracking=True)
    year_study = fields.Char('Year of Study', tracking=True)
    receipt_no = fields.Char('Receipt No.', tracking=True)
    receipt_date = fields.Char('Receipt Date', tracking=True)
    type_payment = fields.Char('Payment Type', tracking=True)
    instrument_no = fields.Char('Instrument No.', tracking=True)
    instrument_date = fields.Char('Instrument Date', tracking=True)
    account_name = fields.Char('Account Name', tracking=True)
