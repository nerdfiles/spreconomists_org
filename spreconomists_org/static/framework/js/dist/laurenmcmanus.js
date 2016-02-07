 /*! laurenmcman_us - v0.0.0 - 2015-12-24
 * https://github.com/nerdfiles/laurenmcman_us
 * Copyright (c) 2015 ; Licensed WTFPL */
(function() {
  (function($, w, document) {

    /*
    Deferred Intense Images Container
    @inner
     */
    var deferredIntenseImagesContainer, intensifyGalleryItem, interactionModel;
    deferredIntenseImagesContainer = function(selector) {
      var d, elementSearch;
      d = new $.Deferred();
      elementSearch = w.setTimeout(function() {
        var figure$;
        figure$ = $(selector);
        console.log(figure$);
        if (figure$.length) {
          return d.resolve(figure$);
        }
      }, 1000);
      return d.promise();
    };

    /*
    Intensify Gallery Item
    @inner
     */
    intensifyGalleryItem = function() {
      var preview$;
      preview$ = $(this);
      console.log(preview$);
      return preview$.on('click.previewIntenseImage', function(e) {
        var img$, miniChargeContainer$, miniChargeContainerClone$;
        img$ = $(e.target);
        miniChargeContainer$ = img$.prev();
        miniChargeContainerClone$ = miniChargeContainer$.clone();
        console.log(miniChargeContainerClone$);
        return deferredIntenseImagesContainer('.intense-images--container').done(function(element$) {
          console.log(element$);
          return miniChargeContainerClone$.appendTo(element$);
        });
      });
    };
    interactionModel = {

      /*
      Intensify
      @memberof interactionModel
       */
      intensify: function() {

        /*
        Preview of Gallery Item
        @description
        Image previews which trigger "zoom" events and "purchase".
         */
        $(document).ready(function() {
          return $('.preview').each(intensifyGalleryItem);
        });
      },
      foundation: function() {},

      /*
      Initialization of DOM handlings
      @memberof interactionModel
       */
      init: function() {
        this.foundation();
        this.intensify();
      }
    };
    return interactionModel.init();
  })(jQuery, window, document);

}).call(this);
