$(document).ready(function () {
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
});