
function changeUF(the_select){
    var uf = the_select.options[the_select.selectedIndex].value;
	var name = the_select.name.substr(0, the_select.name.length-3) ;
	var id = "#id_"+name;
	var reg_el = jQuery('#id_'+the_select.name+'_reg');
	if(uf!=""){
		var mun_sel = jQuery(the_select).parent().parent().find(id);
	    mun_sel.attr('disabled', true).html('<option value="">Aguarde...</option>');
	    mun_sel.load('/municipios_app/ajax/municipios/'+uf+'/', null, function(){
	        mun_sel[0].disabled=false;
	    });
		
		if(reg_el.length){
			reg_el.load(site_root + 'ajax/regiao/'+uf+'/');
		}		
	} else {
		jQuery(id).html('<option value="">--</option>');
		reg_el.html("--");
	}
}
