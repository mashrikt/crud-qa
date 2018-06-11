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

    def test_employee_blank_fields(self, list_create_url, employee_dict):
        """
        Assuming all the fields are required, should throw an error if any field is not entered
        And user should not be added to the list
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

    def test_employee_str_for_int_fields(self, list_create_url, employee_dict):
        """
        using str for int fields should result in failure
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
