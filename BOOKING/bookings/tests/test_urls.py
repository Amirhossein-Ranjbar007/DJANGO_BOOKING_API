from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from bookings.views import BookingCreateView



class TestUrl(SimpleTestCase):

    def test_book_create_url(self):
        url = reverse("booking:book_create")

        self.assertEqual(url, '/booking/book-create/')
        self.assertEqual(resolve(url).func.view_class, BookingCreateView)



    def test_book_list_url(self):
        match = resolve('/booking/book-list/')

        self.assertEqual(match.url_name, 'book_list')


    def test_book_detail_url(self):
        url = reverse('booking:book_detail', kwargs={'id':1})

        self.assertEqual(url, '/booking/book-detail/1/')


    def test_book_detail_url_resolve(self):
        match = resolve('/booking/book-detail/1/')

        self.assertEqual(match.url_name, 'book_detail')
        self.assertEqual(match.kwargs['id'], 1)


    def test_book_cancel_url_resolve(self):
        match = resolve('/booking/book-cancel/1/')

        self.assertEqual(match.url_name, 'book_cancel')
        self.assertEqual(match.kwargs['id'], 1)


    def test_book_cancel_url(self):
        url = reverse('booking:book_cancel', kwargs={'id':1})

        self.assertEqual(url, '/booking/book-cancel/1/')


        

