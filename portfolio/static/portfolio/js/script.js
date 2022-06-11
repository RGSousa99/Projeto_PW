/*function showTime(){
    const time = new Date();
    let hour = time.getHours();
    let minute = time.getMinutes();
    let second = time.getSeconds();

    if (hour<10) hour= "0"+hour;
    if (minute<10) minute= "0"+minute;
    if (second<10) second= "0"+second;

    document.getElementById('timer').innerHTML=hour + ":" + minute + ":" + second;
}
function initTime() {
    setInterval(showTime, 1000);
}*/

(function(){
	// Função que permite selecionar elementos do documento
	function $(seletor){
		return document.querySelector(seletor);
	}

	function digitalClock(){
		var dHoje = new Date();
		var dia = dHoje.getDate()
		var mes = dHoje.getMonth();
		var ano = dHoje.getFullYear();
		// Utilização de operador ternário para adiionar o prefixo zero quando o digito for inferior a dez
		var hora = dHoje.getHours() < 10 ? "0" + dHoje.getHours() : dHoje.getHours();
		var min = dHoje.getMinutes() < 10 ? "0" + dHoje.getMinutes() : dHoje.getMinutes();
		var sec = dHoje.getSeconds() < 10 ? "0" + dHoje.getSeconds() : dHoje.getSeconds();
		// Formatação da saída
		var horas = "<span class='horas-segundos'>" + hora + "</span>" +
					"<span class='pontos'>:</span>" +
					"<span class='minutos'>" + min + "</span>" +
					"<span class='pontos'>:</span>" +
					"<span class='horas-segundos'>" + sec + "</span>";
		// Coloca horas
		$('.digital').innerHTML = horas;
	}

	// Efetua uma leitura a cada segundo
	setInterval(function(){
		digitalClock();
	}, 1000);

})();