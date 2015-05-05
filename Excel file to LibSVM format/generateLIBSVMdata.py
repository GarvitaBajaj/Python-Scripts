import xlrd
import xlwt
import xlsxwriter

book=xlrd.open_workbook('[book_name].xlsx')
sheet=book.sheet_by_index([index_number])
text_file = open("Output.txt", "w")
print sheet.ncols
for row in range(1,sheet.nrows):
		for col in range(0,sheet.ncols-1):
			if(sheet.cell_type(row,col) in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK)):
				break
			else:
				print row,col
				if(col==0):
					text_file.write('\n'+str(sheet.cell_value(row,col)))
				elif(col==sheet.ncols-2):
					text_file.write(' ' +str(col)+':'+str(sheet.cell_value(row,col)))
				else:
					text_file.write(' ' +str(col)+':'+str(sheet.cell_value(row,col)))

text_file.close()		