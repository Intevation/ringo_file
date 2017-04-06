% if mime:
  <div class="filepreview">
    % if mime.find("image") > -1:
      <a href="${url}" class="nospinner"><img src="${url}" class="img-responsive img-thumbnail"></a>
    % else:
      <object data="${url}" type="${mime}">
        <p>It appears you don't have support for the filetype in this web
          browser. <a href="${url}" class="nospinner">Click here to download the File.</a></p>
        <embed src="${url}" type="${mime}" />
      </object>
    % endif
  </div>
% endif
