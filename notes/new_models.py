class AccountSection(models.Model):
    sid = models.IntegerField(unique=True)
    name = models.TextField()


class AccountGroup(models.Model):
    name = models.CharField(max_length=30, unique=True)
    section = models.ForeignKey(AccountSection, db_index=True)
    p_and_l = models.SmallIntegerField()
    sequence_in_tb = models.SmallIntegerField(db_index=True)
    parent = models.ForeignKey('self', db_index=True, null=True, blank=True)


class Area(models.Model):
    code = models.CharField(max_length=3, unique=True)
    description = models.CharField(max_length=25)


class AssetManager(models.Model):
    stock_id = models.CharField(max_length=20)
    serial_no = models.CharField(max_length=30)
    location = models.CharField(max_length=15)
    cost = models.DecimalField(max_digits=12, decimal_places=4)
    depn = models.DecimalField(max_digits=12, decimal_places=4)
    data_purchased = models.DateField()
    disposal_value = models.IntegerField()


class TaxProvince(models.Model):
    tpid = models.SmallIntegerField(unique=True)
    name = models.CharField(max_length=30)


class Location(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50, unique=True)
    add_1 = models.CharField(max_length=40)
    add_2 = models.CharField(max_length=40)
    add_3 = models.CharField(max_length=40)
    add_4 = models.CharField(max_length=40)
    add_5 = models.CharField(max_length=40)
    add_6 = models.CharField(max_length=40)
    tel = models.CharField(max_length=30)
    fax = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.CharField(max_length=30)
    tax_province_id = models.ForeingnKey(TaxProvince, db_index=True)
    cash_sale_customer = models.CharField(max_length=10, blank=True)
    managed = models.IntegerField(null=True, blank=True)
    cash_sale_branch = models.CharField(max_length=10, blank=True)
    internal_request = models.BooleanField(default=True, help_text='Allow internal request from this location.')


class WwwUser(models.Model):
    wuid = models.CharField(max_length=20, unique=True)
    password = models.PasswordField()
    real_name = models.CharField(max_length=35)
    customer_id = models.CharField(max_length=10, db_index=True)
    supplier_id = models.CharField(max_length=10)
    salesman = models.CharField(max_length=3)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=55, blank=True)
    default_location = models.ForeignKey(Location, db_index=True)
    full_access = models.IntegerField()
    can_create_tender = models.BooleanField()
    last_visit_date = models.DateTimeField()
    branch_code = models.CharField(max_length=10)
    page_size = models.CharField(max_length=20)
    modules_allowed = models.CharField(max_length=40)
    blocked = models.SmallIntegerField()
    display_records_max = models.IntegerField()
    theme = models.CharField(max_length=30)
    language = models.CharField(max_length=10)
    pdf_language = models.BooleanField()
    department = models.IntegerField()


class AuditTrail(models.Model):
    transaction_date = models.DateTimeField()
    user_id = models.ForeignKey(WwwUser, db_index=True)
    query_string = models.TextField(blank=True)


class ChartMaster(models.Model):
    account_code = models.CharField(max_length=20)
    account_name = models.CharField(max_length=50)
    group = models.ForeignKey(AccountGroup)


class BankAccount(models.Model):
    account_code = models.ForeignKey(ChartMaster, unique=True)
    curr_code = models.CharField(max_length=3, db_index=True)
    invoice = models.SmallIntegerField()
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50, db_index=True)
    number = models.CharField(max_length=50, db_index=True)
    bank_address = models.CharField(max_length=50, blank=True)


class SysType(models.Model):
    stid = models.SmallIntegerField(unique=True)
    name = models.CharField(max_length=50)
    no = models.IntegerField(db_index=True)


class BankTran(models.Model):
    btid = models.BigIntegerField(unique=True)
    stype = models.ForeignKey(SysType)
    no = models.BigIntegerField()
    bank_act = models.ForeignKey(BankAccount)
    ref = models.CharField(max_length=50, db_index=True)
    amount_cleared = models.DecimalField(max_digits=12, decimal_places=4)
    ex_rate = models.DecimalField(max_digits=12, decimal_places=4, help_text='From bank account currency to payment currency.')
    functional_ex_rate = models.DecimalField(max_digits=12, decimal_places=4, help_text='Account currency to functional currency.')
    btdate = models.DateField(db_index=True)
    bttype = models.CharField(max_length=30, db_index=True)
    amount = models.DecimalField(max_digits=12, decimal_places=4)
    curr_code = models.CharField(max_length=3, db_index=True)

    class Meta:
        index_together = (('bank_act', 'ref'), ('stype', 'no'))


class TaxCategory(models.Model):
    tcid = models.SmallIntegerField()
    name = models.CharField(max_length=30)


class StockCategory(models.Model):
    scid = models.CharField(max_length=6, unique=True)
    description = models.CharField(max_length=20)
    stock_type = models.CharField(max_length=1)
    stock_act = models.CharField(max_length=20)
    adj_gl_act = models.CharField(max_length=20)
    issue_gl_act = models.CharField(max_length=20)
    purch_price_var_act = models.CharField(max_length=20)
    material_usage_var_act = models.CharField(max_length=20)
    wip_act = models.CharField(max_length=20)
    default_tax_cat = models.ForeignKey(TaxCategory)


class StockMaster(models.Model):
    stock_id = models.CharField(max_length=20, unique=True)
    category = models.ForeignKey(StockCategory)
    description = models.CharField(max_length=50)
    long_description = models.TextField()
    units = models.CharField(max_length=20)
    mb_flag = models.CharField(max_length=1)
    actual_cost = models.DecimalField(max_digits=20, decimal_places=4)
    last_cost = models.DecimalField(max_digits=20, decimal_places=4)
    material_cost = models.DecimalField(max_digits=20, decimal_places=4)
    labour_cost = models.DecimalField(max_digits=20, decimal_places=4)
    overhead_cost = models.DecimalField(max_digits=20, decimal_places=4)
    lowest_level = models.SmallIntegerField()
    discountinued = models.BooleanField(default=False)
    controlled = models.BooleanField(default=False)
    eoq = models.FloatField()
    volume = models.DecimalField(max_digits=20, decimal_places=4)
    gross_weight = models.DecimalField(max_digits=20, decimal_places=4)
    barcode = models.CharField(max_length=50)
    discount_category = models.CharField(max_length=2)
    tax_cat = models.ForeignKey(TaxCategory)
    serialized = models.BooleanField(default=False)
    append_file = models.CharField(max_length=40)
    perishable = models.BooleanField(default=False)
    decimal_places = models.SmallIntegerField()
    pan_size = models.FloatField()
    shrink_factore = models.FloatField()
    next_serial_no = models.BigIntegerField()
    net_weight = models.DecimalField(max_digits=20, decimal_places=4)
    last_cost_update = models.DateField()


class Bom(models.Model):
    parent = models.ForeignKey(StockMaster, related_name='bom_list', db_index=True)
    component = models.ForeignKey(StockMaster, related_name='in_bom_list', db_index=True)
    work_centre_added = models.ForeignKey(WorkCentre, db_index=True)
    loc = models.ForeignKey(Location, db_index=True)
    effective_after = models.DateField(db_index=True)
    effective_to = model.DateField(db_index=True)
    quantity = models.DecimalField(max_digits=12, decimal_places=4)
    auto_issue = models.SmallIntegerField()

    class Meta:
        unique_together = ('parent', 'component', 'workcentreadded', 'loc')
        index_together = ('parent', 'effective_after', 'effective_to', 'loc')
