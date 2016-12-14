<div class="filepreview">
  % if mime.find("image") > -1:
    <img src="${url}" class="img-responsive">
  % else:
    <object data="${url}" type="${mime}">
      <p>It appears you don't have Adobe Reader or PDF support in this web browser. <a href="${url}">Click here to download the PDF</a>. Or <a href="http://get.adobe.com/reader/" target="_blank">click here to install Adobe Reader</a>.</p>
      <embed src="${url}" type="${mime}" />
    </object>
  % endif
</div>
