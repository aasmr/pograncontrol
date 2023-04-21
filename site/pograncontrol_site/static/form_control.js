$(document).ready(function() {
// Функция отправки формы на заданный URL
function submitForm(url) {
  // Получаем данные из формы
  var formData = $('#category-form').serialize();

  // Отправляем данные на указанный URL с использованием AJAX-запроса
  $.ajax({
    url: url,
    type: 'POST',
    data: formData,
    success: function(response) {
      // Обработка успешного ответа от сервера
      console.log('Данные успешно отправлены на ' + url);
      console.log('Ответ сервера: ' + response);
      // Здесь можно добавить дополнительную логику
    },
    error: function(jqXHR, textStatus, errorThrown) {
      // Обработка ошибки при отправке данных
      console.log('Произошла ошибка при отправке данных на ' + url);
      console.log('Ошибка: ' + textStatus + ' - ' + errorThrown);
      // Здесь можно добавить дополнительную логику
    }
  });
}

// Добавляем обработчики событий на клик кнопок
$('#category-form button').on('click', function(event) {
  event.preventDefault(); // Предотвращаем стандартное поведение отправки формы
  var url = $(this).data('url'); // Получаем URL из атрибута data-url кнопки
  submitForm(url); // Вызываем функцию отправки формы с передачей URL
});
});