function init(title, page_name) {
	$(document).ready(function () {
		document.title = title;
		$("#tab_" + page_name).attr("class", "active");
	})
}

String.prototype.format = function () {
	var args = arguments;
	return this.replace(/\{(\d+)\}/g, function (s, i) {
		return args[i];
	});
}
