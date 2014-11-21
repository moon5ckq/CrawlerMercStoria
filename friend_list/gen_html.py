import sys

print '''
<script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
'''

with open(sys.argv[1]) as f:
    for idx, line in enumerate(f):
        file = line.strip().split(' ')
        
        print r'''<div id="_%s"><img src="%s" height="200"> <img src="%s" height="200"> 
        <input class="aa" type="button" value="del" data="%s"> <br/> </div>  ''' % (idx, file[0], file[1], idx)

print '''
    <br/><input type="button" id="gen" value="gen">
    <br/><div id="show"/>
    <script>
        $('.aa').on('click', function() {
            console.log($('#_' + $(this).attr('data')).remove());
        });
        
        $('#gen').on('click', function() {
            var all = $('[id^=_]');
            var show = $('#show'), text='';
            for (var i = 0; i < all.length; ++i) {
                var img = $(all[i]).children('img');
                text += $(img[0]).attr('src') + ' ' + $(img[1]).attr('src') + '<br />';
                //console.log($(img[0]).attr('src'));
                //console.log($(img[1]).attr('src'));
            }
            show.html(text);
        });
    </script>
'''