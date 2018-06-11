import requests

from random import randint


class TestEmployeeCreate(object):
    def test_employee_status_code(self, list_create_url, employee_dict):
        """
        on create status code should be 201
        :param list_create_url:
        :param employee_dict:
        :return:
        """
        response = requests.post(url=list_create_url, json=employee_dict)
        print(response.status_code)
        # when object created status_code should be 201, commented it out to continue test
        assert response.status_code == 201

    def test_employee_create(self, list_create_url, employee_dict):
        """
        test if all the fields entered are returned appropriately
        :param list_create_url:
        :param employee_dict:
        :return:
        """
        response = requests.post(url=list_create_url, json=employee_dict)
        assert response.json()['username'] == employee_dict['username']
        assert response.json()['first_name'] == employee_dict['first_name']
        assert response.json()['last_name'] == employee_dict['last_name']
        assert response.json()['email'] == employee_dict['email']
        assert response.json()['department'] == employee_dict['department']
        assert response.json()['salary'] == employee_dict['salary']
        assert response.json()['age'] == employee_dict['age']

    def test_negative_salary(self, list_create_url, employee_dict):
        """
        should not accept negative salary
        :param list_create_url:
        :param employee_dict:
        :return:
        """
        employee_dict['salary'] = -100
        response = requests.post(url=list_create_url, json=employee_dict)
        assert response.status_code == 400
        response2 = requests.get(url=list_create_url)
        # FIXME hack required since age is a string field
        employee_dict['age'] = str(employee_dict['age'])
        assert employee_dict not in response2.json()

    def test_negative_age(self, list_create_url, employee_dict):
        """
        should not accept negative salary
        :param list_create_url:
        :param employee_dict:
        :return:
        """
        employee_dict['age'] = -100
        response = requests.post(url=list_create_url, json=employee_dict)
        assert response.status_code == 400
        response2 = requests.get(url=list_create_url)
        # FIXME hack required since age is a string field
        employee_dict['age'] = str(employee_dict['age'])
        assert employee_dict not in response2.json()

    def test_employee_str_for_int_fields(self, list_create_url, employee_dict):
        """
        using string for int fields(salary, age) should result in failure
        :param list_create_url:
        :param employee_dict:
        :return:
        """
        fields = ['salary', 'age']
        for field in fields:
            new_dict = employee_dict
            new_dict[field] = randint(1, 10)
            response = requests.post(url=list_create_url, json=new_dict)
            print(field)
            assert response.status_code == 400
            # user should not be created either
            response2 = requests.get(url=list_create_url)
            # FIXME hack required since age is a string field
            new_dict['age'] = str(new_dict['age'])
            assert new_dict not in response2.json()

    def test_employee_int_for_str_fields(self, list_create_url, employee_dict):
        """
        using int for string fields should result in failure
        :param list_create_url:
        :param employee_dict:
        :return:
        """
        fields = ['username', 'first_name', 'last_name', 'department']
        for field in fields:
            new_dict = employee_dict
            new_dict[field] = randint(1, 10)
            response = requests.post(url=list_create_url, json=new_dict)
            assert response.status_code == 400

    def test_employee_blank_fields(self, list_create_url, employee_dict):
        """
        Assuming all the fields are required, should throw an error if any field is not entered
        :param list_create_url:
        :param employee_dict:
        :return:
        """
        fields = ['username', 'first_name', 'last_name', 'email', 'department', 'age', 'salary']
        for field in fields:
            new_dict = employee_dict
            del new_dict[field]
            response = requests.post(url=list_create_url, json=new_dict)
            assert response.status_code == 400

    def test_improper_email(self, list_create_url, employee_dict):
        """
        improper type email should return a validation error
        :param list_create_url:
        :param employee_dict:
        :return:
        """
        employee_dict['email'] = 'improper email'
        response = requests.post(url=list_create_url, json=employee_dict)
        assert response.status_code == 400

    def test_same_user_twice(self, list_create_url, employee_dict):
        """
        same user should not be created twice
        :param list_create_url:
        :param employee_dict:
        :return:
        """
        response = requests.post(url=list_create_url, json=employee_dict)
        response2 = requests.post(url=list_create_url, json=employee_dict)
        assert response.status_code == 200
        assert response2.status_code == 400
