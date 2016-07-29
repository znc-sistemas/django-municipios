
function changeUF(the_select){
    var uf = the_select.options[the_select.selectedIndex].value;
    var name = the_select.name.substr(0, the_select.name.length-3);

    var app_label = the_select.getAttribute('data-app_label');
    var object_name = the_select.getAttribute('data-object_name');

    var id = "#id_"+name;
    if(uf!=""){
        var mun_sel = jQuery(id);
        mun_sel.attr('disabled', true).html('<option value="">Aguarde...</option>');
        mun_sel.load(
            __municipios_base_url__+'ajax/municipios/'+uf+'/'+app_label+'/'+object_name+'/',
            null,
            function(){
                mun_sel[0].disabled=false;
                mun_sel.trigger( "endLoadMunicipios" );
            }
        );
    } else {
        jQuery(id).html('<option value="">--</option>');
    }
}
