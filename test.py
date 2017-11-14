import link
from datetime import datetime, timedelta
import search
import multi_search

import unittest

class TestFlightScraper(unittest.TestCase):
    
    flights_web = "https://www.google.com/flights/#search;"
    t_day = "01"
    t_month = "12"
    t_year = "2017"
    travel_date = datetime.strptime(t_day+"/"+t_month+"/"+t_year,"%d/%m/%Y")
    b_day = "28"
    b_month = "01"
    b_year = "2018"
    back_date = datetime.strptime(b_day+"/"+b_month+"/"+b_year,"%d/%m/%Y")
    start_airport = ("GRU","CGH")
    back_airport = ("HND","NRT")
    delta = 2
        
    #Tests if the link has been created correctly
    def test_link_creation(self):
        created_link = link.search_link(self.start_airport,self.back_airport,self.travel_date,self.back_date)
        self.assertIn(self.flights_web, created_link)
        
    # Tests if the function returns a float and a string containing a google flights link with the correct info
    def test_lowprice(self):
        price, link = search.fsearch_lowprice(self.start_airport,self.back_airport,self.travel_date,self.back_date)
        with self.subTest():
            self.assertTrue(type(price) is float)
        with self.subTest():
            self.assertIn(self.flights_web, link)
        with self.subTest():
            self.assertIn(self.t_year+"-"+self.t_month+"-"+self.t_day, link)
        with self.subTest():
            self.assertIn(self.b_year+"-"+self.b_month+"-"+self.b_day, link)
            
    def test_delta_search(self):
        price_list, link_list, dates_list = multi_search.delta_flight_thread(self.delta, self.start_airport,self.back_airport,self.travel_date,self.back_date)
        with self.subTest():
            self.assertEqual(len(price_list), 25)
            for i in range(1, len(price_list)):
                with self.subTest():
                    self.assertTrue(type(price_list[i]) is float)
        with self.subTest():
            self.assertEqual(len(link_list), 25)
            for i in range(1, len(link_list)):
                with self.subTest():
                    self.assertIn(self.flights_web, link_list[i])
                    """
                with self.subTest():
                    self.assertIn(self.t_year+"-"+self.t_month+"-"+self.t_day, link_list[i])
                with self.subTest():
                    self.assertIn(self.b_year+"-"+self.b_month+"-"+self.b_day, link_list[i])
                    """
        with self.subTest():
            self.assertEqual(len(dates_list), 9)
        """with self.subTest():
            
        with self.subTest():
            
        with self.subTest():
            """
        
if __name__ == '__main__':
    unittest.main()