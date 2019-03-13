median_filter = itk.MedianImageFilter[ImageType, ImageType].New()
median_filter.SetInput(image)
median_filter.SetRadius(5)
median_filter.Update()
median_filtered_image = median_filter.GetOutput()
view(median_filtered_image)