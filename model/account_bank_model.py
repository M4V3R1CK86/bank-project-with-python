class AccountBankModel:
    def __init__(self, user_id, bank_code, account_type, balance, overdraft_limit, account_number, branch_number):
        self.user_id = user_id
        self.bank_code = bank_code
        self.account_type = account_type
        self.balance = balance
        self.overdraft_limit = overdraft_limit
        self.account_number = account_number
        self.branch_number = branch_number
