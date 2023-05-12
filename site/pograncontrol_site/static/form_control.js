$(document).ready(function() {
// Функция отправки формы на заданный URL
function getMarked()
{
	$.ajax({
    url: '/razmetka/get-marked/',
    type: 'GET',
    success: function(response) {
	  $('#marked_text').text(response.marked_text);
	}
	});
}
function getDuplicate()
{
	$.ajax({
    url: '/razmetka/get-dup/',
    type: 'GET',
    success: function(response) {
	  $("#category-form")[0].reset();
	  let dtInput = document.querySelector('input[name="age"]');
	  dtInput.value = response.age;
	  
	  dtInput = document.querySelector('input[name="cause"]');
	  dtInput.value = response.cause;
	  
	  dtInput = document.querySelector('input[name="army-other"]');
	  dtInput.value = response.army_other;
	  
	  dtInput = document.querySelector('input[name="country"]');
	  dtInput.value = response.country;
	  
	  dtInput = document.querySelector('input[name="kpp"]');
	  dtInput.value = response.kpp;
	  
	  dtInput = document.querySelector('input[name="yService"]');
	  dtInput.value = response.yservice;
	  
	  dtInput = document.querySelector('input[name="voenk-region"]');
	  dtInput.value = response.voenk_region;
	  
	  dtInput = document.querySelector('input[name="kategoryH"]');
	  dtInput.value = response.kategoryh;
	  
	  dtInput = document.querySelector('input[name="kategoryZ"]');
	  dtInput.value = response.kategoryz;
	  
	  dtInput = document.querySelector('input[name="kategoryZ"]');
	  dtInput.value = response.kategoryz;
	}
	});
}
function getInfo()
{
	$.ajax({
    url: '/razmetka/get-mes/',
    type: 'GET',
    success: function(response) {
	  $("#category-form")[0].reset();
	  $('#label_date').text(response.date);
	  $('#label_mestext').text(response.mes_text);
	  
	  let dtInput = document.querySelector('input[name="date"]');
	  dtInput.value = response.date;
	  
	  let duplicate_exist = response.duplicate_exist;
	  if (duplicate_exist == 1)
		  getDuplicate();
	}
	});
}
function autocmplt()
{
	var $ac_cause = $("#cause");
	var $ac_army_relations = $("#army-relations");
	var $ac_vus = $("#vus");
	var $ac_army_type = $("#army-type");
	var $ac_army_sec_type = $("#army-sec-type");
	var $ac_army_other = $("#army-other");
	var $ac_country = $("#country");
	var $ac_kpp = $("#kpp");
	var $ac_yService = $("#yService");
	var $ac_voenk_region = $("#voenk-region");
	var $ac_voenk_city = $("#voenk-city");
	var $ac_voenk_district = $("#voenk-district");
	
	$.ajax({
		url: "/razmetka/autocmplt/",
		success:function (data) {
			$ac_cause.autocomplete({
			source: data.autocmplt_cause,
			});
			$ac_army_relations.autocomplete({
			source: data.autocmplt_army_relations,
			});
			$ac_vus.autocomplete({
			source: data.autocmplt_vus,
			});
			$ac_army_type.autocomplete({
			source: data.autocmplt_army_type,
			});
			$ac_army_sec_type.autocomplete({
			source: data.autocmplt_army_sec_type,
			});
			$ac_army_other.autocomplete({
			source: data.autocmplt_army_other,
			});
			$ac_country.autocomplete({
			source: data.autocmplt_country,
			});
			$ac_kpp.autocomplete({
			source: data.autocmplt_kpp,
			});
			$ac_yService.autocomplete({
			source: data.autocmplt_yService,
			});
			$ac_voenk_region.autocomplete({
			source: data.autocmplt_voenk_region,
			});
			$ac_voenk_city.autocomplete({
			source: data.autocmplt_voenk_city,
			});
			$ac_voenk_district.autocomplete({
			source: data.autocmplt_voenk_district,
			});
		}
	});
}  
function submitFormAdd(url) {
  // Получаем данные из формы
  var formData = $('#category-form').serialize();

  // Отправляем данные на указанный URL с использованием AJAX-запроса
  $.ajax({
    url: url,
    type: 'POST',
    data: formData,
    success: function() {
		$('#label_date').text("");
		$('#label_mestext').text("");
		getMarked();
		getInfo();
		window.scrollTo({
			top: 0,
			left: 0,
			behavior: 'smooth'
		});
		autocmplt();
	},
    error: function(jqXHR, textStatus, errorThrown) {
      // Обработка ошибки при отправке данных
      console.log('Произошла ошибка при отправке данных на ' + url);
      console.log('Ошибка: ' + textStatus + ' - ' + errorThrown);
      // Здесь можно добавить дополнительную логику
    }
  });
}
function submitFormAddMore(url) {
  // Получаем данные из формы
  var formData = $('#category-form').serialize();

  // Отправляем данные на указанный URL с использованием AJAX-запроса
  $.ajax({
    url: url,
    type: 'POST',
    data: formData,
	success: function(response) {
	  $("[Успешно]").tooltip();
	  window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
      });
    },
    error: function(jqXHR, textStatus, errorThrown) {
      // Обработка ошибки при отправке данных
      console.log('Произошла ошибка при отправке данных на ' + url);
      console.log('Ошибка: ' + textStatus + ' - ' + errorThrown);
	  getMarked();
	  getInfo();
	  window.scrollTo({
		top: 0,
		left: 0,
		behavior: 'smooth'
	  });
	  autocmplt();
    }
  });
}
getMarked();
getInfo();
autocmplt();
// Добавляем обработчики событий на клик кнопок
$('#category-form button').on('click', function(event) {
  event.preventDefault(); // Предотвращаем стандартное поведение отправки формы
  var url = $(this).data('url'); // Получаем URL из атрибута data-url кнопки
  var id = this.id;
  if (id == "add")
	submitFormAdd(url); // Вызываем функцию отправки формы с передачей URL
  else if (id == "add-more")
	submitFormAddMore(url); // Вызываем функцию отправки формы с передачей URL
  else if (id == "pass")
	submitFormAdd(url); // Вызываем функцию отправки формы с передачей URL
  else if (id == "vbros")
	submitFormAdd(url); // Вызываем функцию отправки формы с передачей URL
  else if (id == "del")
	submitFormAdd(url); // Вызываем функцию отправки формы с передачей URL
});
});