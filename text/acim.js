$("span").dblclick(function(){
	$("span").css("text-decoration","none");
	var pos = $(this).position()
	$(this).css("text-decoration","underline");
	let dnid = "d"+$(this).attr('data-sentence-id')
	let dinsert_text = $("div").filter(function(){
		return $(this).attr('tid') == dnid
	}).first().text()
	let unid = "u"+$(this).attr('data-sentence-id')
	let uinsert_text = $("div").filter(function(){
		return $(this).attr('tid') == unid
	}).first().text()
	$("#dtext").text(dinsert_text)
	$("#dtext").css({top:pos.top+$(this).height()+2,left:pos.left,position:"absolute",backgound:"grey"});
	$("#dtext").show()
	$("#utext").text(uinsert_text)
	$("#utext").css({top:pos.top+$(this).height()+$("#dtext").height()+28,left:pos.left,position:"absolute",backgound:"grey"});
	$("#utext").show()

});
$("body").scroll(function(){
	$("span").css("text-decoration","none");
	$("#dtext").hide()
	$("#utext").hide()
})
$("body").click(function(){
	$("span").css("text-decoration","none");
	$("#dtext").hide()
	$("#utext").hide()
})
$("body").mouseenter(function(){
	$("span").css("text-decoration","none");
	$("#dtext").hide()
	$("#utext").hide()
})
	