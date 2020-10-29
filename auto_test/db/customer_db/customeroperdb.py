from auto_test.db.handlesql import DbOperation


class CustomerOprationDb:
    def __init__(self):
        self.dbop = DbOperation(host='localhost',user='root',password='123456',database='quote',port=3306,charset='utf8')

    def dele_customer_by_id(self,id):
        self.dbop.update_data("delete from tb_customer where customerNO = '{}' ".format(id))

    def update_table_by_id(self,id):
        self.dbop.update_data("update customer_info set user_id = null where customer_id = {}".format(id))