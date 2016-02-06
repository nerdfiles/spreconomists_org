###
@fileOverview
global JS file for the Website.
###
(($, w, document) ->

  ## Internal/Implementation Functions ##

  ###
  Deferred Intense Images Container
  @inner
  ###
  deferredIntenseImagesContainer = (selector) ->
    d = new $.Deferred()

    elementSearch = w.setTimeout(() ->
      figure$ = $(selector)
      console.log(figure$)
      if figure$.length
        d.resolve(figure$)
    , 1000)

    return d.promise()

  ###
  Intensify Gallery Item
  @inner
  ###
  intensifyGalleryItem = () ->
    preview$ = $(this)
    console.log(preview$)

    preview$.on('click.previewIntenseImage', (e) ->

      img$ = $(e.target)
      miniChargeContainer$ = img$.prev()
      miniChargeContainerClone$ = miniChargeContainer$.clone()
      console.log(miniChargeContainerClone$)

      # Wait for Intense Image container to be injected at the tail of <body>
      # in the DOM.
      deferredIntenseImagesContainer('.intense-images--container').done((element$) ->
        console.log(element$)
        miniChargeContainerClone$.appendTo(element$)
      )

    )

  ## DOM Interaction Namespace ##

  interactionModel =

    ###
    Intensify
    @memberof interactionModel
    ###
    intensify: () ->
      ###
      Preview of Gallery Item
      @description
      Image previews which trigger "zoom" events and "purchase".
      ###
      $(document).ready ->
        $('.preview').each intensifyGalleryItem
      return

    foundation: () ->
      #$(document).foundation()
      return

    ###
    Initialization of DOM handlings
    @memberof interactionModel
    ###
    init: () ->
      this.foundation()
      this.intensify()
      return

  # init
  interactionModel.init()

)(jQuery, window, document)
