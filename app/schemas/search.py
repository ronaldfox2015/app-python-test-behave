from marshmallow import Schema, fields


class MetadataSchema(Schema):
	page = fields.Int(required=True)
	limit = fields.Int(required=True)
	totalPages = fields.Int(required=True)	
	resultFound = fields.Int(required=True)


class ResultsSchema(Schema):
	id = fields.Str(required=True)
	projectId = fields.Int(required=False)
	publicationDate = fields.Str(required=True)
	deliveryDate = fields.Str(required=False)
	title = fields.Str(required=True)
	closingYear = fields.Int(required=False)
	operationType = fields.Int(required=True)
	operationTypeName = fields.Str(required=True)
	operationTypeAlias = fields.Str(required=True)
	propertyType = fields.Int(required=True)
	propertyTypeName = fields.Str(required=True)
	propertyTypeAlias = fields.Str(required=True)
	location = fields.Int(required=True)
	propertySubtype = fields.Int(required=False)
	propertySubtypeName = fields.Str(required=False)
	propertySubtypeAlias = fields.Str(required=False)
	departmentId = fields.Int(required=True)
	provinceId = fields.Int(required=True)
	districtId = fields.Int(required=True)
	urbanizationId = fields.Int(required=False)
	roadName = fields.Str(required=True)
	departmentName = fields.Str(required=True)
	departmentAlias = fields.Str(required=True)
	departmentGroup = fields.Str(required=True)
	provinceName = fields.Str(required=True)
	provinceAlias = fields.Str(required=True)
	provinceGroup = fields.Str(required=True)
	districtName = fields.Str(required=True)
	districtAlias = fields.Str(required=True)
	districtGroup = fields.Str(required=True)
	urbanizationAlias = fields.Str(required=False)
	urbanizationName = fields.Str(required=False)
	urbanizationGroup = fields.Str(required=False)
	urbanizationOrBeachName = fields.Str(required=False)
	urbanizationOrBeachAlias = fields.Str(required=False)
	urbanizationOrBeachGroup = fields.Str(required=False)
	latitude = fields.Int(required=True)
	latitudeStr = fields.Str(required=True)
	longitude = fields.Int(required=True)
	longitudeStr = fields.Str(required=True)
	geo = fields.Str(required=True)
	geoRpt = fields.List(fields.Str(required=True))
	hasImages = fields.Int(required=True)
	totalImages = fields.Int(required=True)
	totalVideo = fields.Int(required=True)
	alias = fields.Str(required=True)
	services = fields.List(fields.Str(required=True))
	additionals = fields.List(fields.Str(required=True))
	commonAreas = fields.List(fields.Str(required=True))
	landArea = fields.Int(required=False)
	totalArea = fields.List(fields.Int(required=True))
	description = fields.Str(required=True)
	promotion = fields.Int(required=False)
	promotionTitle = fields.Str(required=False)
	constructionStage = fields.Int(required=False)
	constructionStageName = fields.Str(required=False)
	founded = fields.List(fields.Int(required=True))
	bankName = fields.List(fields.Str(required=True))
	publicationType = fields.Int(required=True)
	typeAdvertiser = fields.Int(required=True)
	priceCurrency = fields.Int(required=False)
	priceAmountPen = fields.List(fields.Int(required=True))
	priceAmountUsd = fields.List(fields.Int(required=True))
	label = fields.Str(required=False)
	highlight = fields.Int(required=True)
	storeId = fields.Int(required=False)
	storeEmail = fields.Str(required=False)
	businessName = fields.Str(required=False)
	tradeName = fields.Str(required=False)
	storeLogo = fields.Str(required=False)
	storeAlias = fields.Str(required=False)
	storeType = fields.Str(required=False)
	typeAnnouncement = fields.Int(required=True)
	origin = fields.Int(required=True)
	centricDistrict = fields.Int(required=False)
	userId = fields.Int(required=True)
	version = fields.Int(required=True)
	profileId = fields.Int(required=True)
	score = fields.Int(required=True)
	priceAmount = fields.List(fields.Decimal(required=True))
		

class SearchSchema(Schema):
	metadata = fields.Nested(MetadataSchema)
	results = fields.List(fields.Nested(ResultsSchema))
