from IPython.display import HTML, display

def tables_side(titolo, tabs, tabslabel):
    return HTML( '<table><caption style="background-color:#F1F2F3;"><h1>'+titolo+'</h1></caption>'+
                 '<tr style="background-color:#D9D9D9;" >'+''.join(['<td><h2 align="center">'+tlabel+ '</h2></td>' for tlabel in tabslabel]) +'</tr>'+
                 '<tr style="background-color:#D9D9D9;">'+''.join(['<td>'+table._repr_html_() + '</td>' for table in tabs]) +
                 '</tr></table>'
               )
