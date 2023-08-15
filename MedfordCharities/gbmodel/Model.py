class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, name, description, address, typeOfCharity, phone, hours, reviews):
        """
        Inserts entry into database
        :param name: String
        :param description: String
        :param address: String
        :param typeOfCharity: String
        :param phone: String
        :param hours: String
        :param reviews: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        pass

