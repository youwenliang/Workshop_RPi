// jshint devel:true
console.log('\'Allo \'Allo!');

// jshint devel:true

var myFirebaseRef = new Firebase("https://rpi-workshop.firebaseio.com/");

$('.click').on('click', function(){
	console.log("!");
});

myFirebaseRef.update({
	K0: "off",
	K1: "off",
	K2: "off",
	K3: "off",
	K4: "off",
	K5: "off",
	K6: "off",
	K7: "off"
});
for(var i = 0; i<8; i++){
	$('#K'+i).text("");
}


// var name = "";
	myFirebaseRef.on("value", function(snapshot) {
		for(var i = 0; i<8; i++){
			if(snapshot.val()["K"+i] == "on"){
				$('#K'+i).addClass('active');
			}
			else $('#K'+i).removeClass('active');
		}
	});
