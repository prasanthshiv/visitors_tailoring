from odoo import models, fields, api,_
import datetime
import smtplib
 
class CronJob(models.Model):
    _name = "cron.job"

    def method_name(self):
        employees=self.env['hr.employee'].search([])
        now = datetime.datetime.today().strftime('%Y-%m-%d')
        for obj in employees:
            # Checking the passport expiry date
            if obj.passport_expiry!=False:
                if obj.passport_expiry==now:
                    self.mail("Subject","mssssageee")
            # Checking the eid expiry date
            if obj.eid_expairy!=False:
                if obj.eid_expairy==now:
                    self.mail("Subject","mssssageee")
            # Checking the insurance expiry date
            if obj.insurance_expairy!=False:
                if obj.insurance_expairy==now:
                    self.mail("Subject","mssssageee")
            # Checking the Labour card expiry date
            if obj.labour_card_expairy!=False:
                if obj.labour_card_expairy==now:
                    self.mail("Subject","mssssageee")
            # Checking the visa card expiry date
            if obj.visa_expiry!=False:
                if obj.visa_expiry==now:
                    self.mail("Subject","mssssageee")
    def mail(self,sub,msg):
        # managers=[]
        # employees=self.env['hr.employee'].search([])
        # for obj in employees:
        #     if obj.manager:
        #         managers.append(obj.work_email)
        # sender_id=self.env['ir.mail_server'].search([])
        # sender = sender_id.smtp_user
        # message = 'Subject: {}\n\n{}'.format(sub, msg)
           
        # smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
        # smtpObj.ehlo()
        # smtpObj.starttls()
        # smtpObj.ehlo()
        # smtpObj.login(user=sender_id.smtp_user, password=sender_id.smtp_pass)
        # smtpObj.sendmail(sender, managers, message)      
        print "Successfully sent email"

class VisaType(models.Model):
    _name = "visa.type"
    
    name = fields.Char('VisaType', required=True)

class HrLocation(models.Model):
    _name = "hr.location"
    
    name = fields.Char('Location', required=True)

class InsuranceType(models.Model):
    _name = "insurance.type"

class HrDocs(models.Model):

    _name = "hr.docs"
    _description = 'HR Docs'
    
    name = fields.Char('Doc Name')
    document = fields.Binary('Document')
    document_name = fields.Char('Document Name')
    employee_id = fields.Many2one('hr.employee', 'Employee')

class TimesheetType(models.Model):

    _name = "timesheet.type"
    
    name = fields.Char('Timesheet Type', required=True)

class Accomodation(models.Model):
    _name = "hr.accomodation"
    
    name = fields.Char('Accomodation', required=True)

class Travel(models.Model):
    _name = "hr.travel"
    
    name = fields.Char('Travel', required=True)

class HrDocs(models.Model):

    _name = "hr.docs"
    _description = 'HR Docs'
    
    name = fields.Char('Doc Name')
    document = fields.Binary('Document')
    document_name = fields.Char('Document Name')
    employee_id = fields.Many2one('hr.employee', 'Employee')

class EmployeeProfile(models.Model):
    _inherit="hr.employee"

    code=fields.Char(string="Employee Code")
    place_of_birth=fields.Char(string="Place of Birth")
    languages=fields.Char(string="Languages Known")
    vehicle_number=fields.Char(string="Vehicle Number")
    license_no=fields.Char(string="License Number")
    l_issue_date=fields.Date(string="Issue Date")
    l_expiry_date=fields.Date(string="Expiry Date")
    passport_issue_date=fields.Date(string="Passport Issue Date")
    passport_expiry=fields.Date(string="Passport Expiry")
    passport_status=fields.Selection([('in_house', 'In House'),('employee', 'Employee'),('leave', 'Leave'),('ren_can', 'Renewal/Cancellation')])
    driving_license=fields.Selection([('yes', 'Yes'),('no', 'No')])
    date_join=fields.Date(string="Joining Date")
    visa_under=fields.Many2one('res.company',string='Visa under')
    visa_type_id=fields.Many2one('visa.type',string='Visa Type')
    work_location_id =fields.Many2one('hr.location', 'Location')
    eid_no=fields.Char(string="EID Number")
    eid_expairy=fields.Date(string="EID Expiry Date")
    eid_cd=fields.Binary(string="EID Card")
    labour_card_no=fields.Char(string="Labour Card/Work Permit No")
    lab_no=fields.Char(string="Personal Number")
    labour_card_expairy=fields.Date(string="Labour Card Expiry Date")
    lab_cd=fields.Binary(string="Labour Card")
    insurance_no=fields.Char(string="Insurance Number")
    insurance_type_id = fields.Many2one('insurance.type', 'Insurance Class')
    insurance_expairy=fields.Date(string="Insurance Expiry")
    insurance_cd = fields.Binary('Insurance Card')
    doc_ids = fields.One2many('hr.docs', 'employee_id', 'Misc. Documents')
    cv = fields.Binary(string='CV')
    offer_letter = fields.Binary(string='Offer Letter')
    mol_doc = fields.Binary(string='MOL Offer')
    induction_doc = fields.Binary(string='Induction Document')
    labor_contract = fields.Binary(string='Labor Contract')
    timesheet_type_id = fields.Many2one('timesheet.type', 'Timesheet Type')
    contrac_type = fields.Selection([('unlimited', 'Unlimited'), ('limited', 'Limited')], 'Contract Type')
    accommodation_id = fields.Many2one('hr.accomodation', 'Accommodation')
    travel_id = fields.Many2one('hr.travel', 'Travel')
    visa_issue_date=fields.Date(string="Visa Issue Date")
    visa_expiry=fields.Date(string="Visa Expiry")
    visa_designation = fields.Many2one('hr.employee.category', 'Designation Under Visa')
    visa=fields.Binary(string='Visa')
    doc_ids = fields.One2many('hr.docs', 'employee_id', 'Misc. Documents')
    manager=fields.Boolean(string="Is a Manager")
    total_commission=fields.Float(string="Total Commission")
