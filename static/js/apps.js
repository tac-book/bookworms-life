$( function() {

  // vertical
  $("#tabs")
      .tabs()
      .addClass("ui-tabs-vertical ui-helper-clearfix")
      .children("ul > li")
        .removeClass("ui-corner-top")
        .addClass("ui-corner-left");
});
