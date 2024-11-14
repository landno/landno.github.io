$("span").dblclick(function(){
	$("span").css("text-decoration","none");
	var pos = $(this).position()
	var fontSize = $(this).css('font-size');
	var lineHeight = Math.floor(parseInt(fontSize.replace('px','')) * 1.5);
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
	$("#dtext").css({top:pos.top-lineHeight-$('#dtext').height(),left:pos.left,position:"absolute",backgound:"grey"});
	$("#dtext").show()
	$("#utext").text(uinsert_text)
	$("#utext").css({top:pos.top-$("#dtext").innerHeight()-lineHeight-$("#utext").innerHeight()+16,left:pos.left,position:"absolute",backgound:"grey"});
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
	