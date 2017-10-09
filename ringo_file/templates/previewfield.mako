## -*- coding: utf-8 -*-
% if mime:
  <div class="filepreview">
    % if mime.find("image") > -1:
      <a href="#" class="nospinner thumbnail" title="${item}"><img src="${url}" class="img-responsive img-thumbnail"></a>
    % else:
        % if mime.find("pdf") > -1:
          <object data="${url}" type="${mime}">
             <embed src="${url}" type="${mime}" />
          </object>
        % else:
          <p>It appears you don't have support for the filetype in this web
            browser. <a href="${url}" class="nospinner">Click here to download the File.</a></p>
        % endif
    % endif
  </div>
  <div id="filepreviewModal" class="modal fade" tabindex="-1" role="dialog">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close nospinner" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title">Modal title</h4>
        </div>
        <div class="modal-body">
          <p>One fine body&hellip;</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default nospinner" data-dismiss="modal">Close</button>
        </div>
      </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
  </div>
  <script>
    $('.thumbnail').click(function(){
      var title = $(this).attr("title");
      $('.modal-title').html(title);
      var img = $('.img-thumbnail').clone();
      img.removeClass('img-thumbnail');
      $('.modal-body').empty();
      $('.modal-body').html(img);
      $('#filepreviewModal').modal("show");
    });
  </script>
% endif
