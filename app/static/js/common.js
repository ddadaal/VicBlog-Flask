function init(title, page_name) {
	$(document).ready(function () {
		document.title = title;
		$("#tab_" + page_name).attr("class", "active");
	})
}