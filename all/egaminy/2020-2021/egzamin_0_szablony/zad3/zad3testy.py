tests = [
    {
        'G': [[0, 1],
              [1, 0]],
        'frm': 0,
        'to': 1,
        'length': 1, 
        'path': [0, 1]
    }, {
        'G': [[0, 2, 0],
              [2, 0, 3],
              [0, 3, 0]],
        'frm': 0,
        'to': 2,
        'length': 3, 
        'path': [0, 2]
    }, {
        'G': [[0, 1, 0, 0],
              [1, 0, 2, 0],
              [0, 2, 0, 3],
              [0, 0, 3, 0]],
        'frm': 0,
        'to': 3,
        'length': 4, 
        'path': [0, 1, 3]
    }, {
        'G': [[0, 1, 3, 0],
              [1, 0, 1, 2],
              [3, 1, 0, 4],
              [0, 2, 4, 0]],
        'frm': 0,
        'to': 3,
        'length': 2, 
        'path': [0, 3]
    }, {
        'G': [[0, 10, 1, 0],
              [10, 0, 10, 0],
              [1, 10, 0, 2],
              [0, 0, 2, 0]],
        'frm': 0,
        'to': 3,
        'length': 2, 
        'path': [0, 3]
    }, {
        'G': [[0, 1, 3, 0],
              [1, 0, 1, 2],
              [3, 1, 0, 4],
              [0, 2, 4, 0]],
        'frm': 3,
        'to': 0,
        'length': 2, 
        'path': [3, 0]
    }, {
        'G': [[0,1,3,4,0],
              [1,0,0,2,0],
              [3,0,0,5,6],
              [4,2,5,0,3],
              [0,0,6,3,0]],
        'frm': 0,
        'to': 4,
        'length': 4, 
        'path': [0, 4]
    }, {
        'G': [[0,2,6,0,0],
              [2,0,3,0,0],
              [6,3,0,1,6],
              [0,0,1,0,1],
              [0,0,6,1,0]],
        'frm': 0,
        'to': 4,
        'length': 5,
        'path': [0,2,3,4]
    }, {
        'G': [[0,2,6,0,0],
              [2,0,3,0,0],
              [6,3,0,0,6],
              [0,0,0,0,0],
              [0,0,6,0,0]],
        'frm': 0,
        'to': 4,
        'length': 6,
        'path': [0,4]
    }, {
        'G': [[0, 1, 0, 0, 0, 0],
              [1, 0, 2, 2, 0, 0],
              [0, 2, 0, 0, 3, 0],
              [0, 2, 0, 0, 3, 0],
              [0, 0, 3, 3, 0, 1],
              [0, 0, 0, 0, 1, 0]],
        'frm': 0,
        'to': 5,
        'length': 5, 
        'path': [0, 1, 4, 5]
    }, {
        'G': [[0, 1, 200, 200, 200, 200],
              [1, 0, 2, 200, 200, 200],
              [200, 2, 0, 40, 200, 200],
              [200, 200, 40, 0, 40, 200],
              [200, 200, 200, 40, 0, 117],
              [200, 200, 200, 200, 117, 0]],
        'frm': 0,
        'to': 5,
        'length': 159,
        'path': [0, 2, 3, 5]
    }, {
        'G': [[0, 1, 200, 200, 200, 200],
              [1, 0, 2, 200, 200, 200],
              [200, 2, 0, 40, 200, 200],
              [200, 200, 40, 0, 40, 200],
              [200, 200, 200, 40, 0, 117],
              [200, 200, 200, 200, 117, 0]],
        'frm': 0,
        'to': 4,
        'length': 43,
        'path': [0, 1, 2, 4]
    }, {
        'G': [[0, 1, 200, 200, 200, 200],
              [1, 0, 2, 200, 200, 200],
              [200, 2, 0, 40, 200, 200],
              [200, 200, 40, 0, 40, 200],
              [200, 200, 200, 40, 0, 117],
              [200, 200, 200, 200, 117, 0]],
        'frm': 1,
        'to': 5,
        'length': 159,
        'path': [1, 2, 3, 5]
    }, {
        'G': [[0, 51, 168, 199, 66, 230, 182, 133, 158, 128, 57, 283, 313, 395, 186, 137, 71, 168, 95, 192],
              [51, 0, 194, 57, 254, 133, 216, 5, 201, 76, 230, 207, 217, 121, 230, 4, 351, 230, 286, 84] ,
              [168, 194, 0, 24, 151, 292, 304, 103, 246, 253, 9, 326, 309, 191, 0, 375, 92, 352, 286, 281] ,
              [199, 57, 24, 0, 88, 46, 103, 184, 392, 263, 400, 216, 232, 214, 87, 124, 234, 122, 81, 107] ,
              [66, 254, 151, 88, 0, 101, 373, 301, 324, 254, 223, 263, 145, 250, 27, 25, 206, 74, 117, 169] ,
              [230, 133, 292, 46, 101, 0, 24, 371, 117, 295, 46, 213, 75, 69, 334, 216, 270, 208, 130, 177] ,
              [182, 216, 304, 103, 373, 24, 0, 46, 41, 244, 114, 24, 298, 115, 328, 33, 368, 295, 342, 103] ,
              [133, 5, 103, 184, 301, 371, 46, 0, 287, 225, 14, 194, 304, 145, 353, 71, 119, 130, 40, 268] ,
              [158, 201, 246, 392, 324, 117, 41, 287, 0, 152, 364, 44, 121, 64, 363, 305, 14, 365, 237, 136] ,
              [128, 76, 253, 263, 254, 295, 244, 225, 152, 0, 277, 75, 314, 247, 124, 206, 320, 281, 157, 289] ,
              [57, 230, 9, 400, 223, 46, 114, 14, 364, 277, 0, 88, 163, 280, 145, 273, 81, 75, 400, 108] ,
              [283, 207, 326, 216, 263, 213, 24, 194, 44, 75, 88, 0, 36, 286, 109, 122, 339, 333, 50, 16] ,
              [313, 217, 309, 232, 145, 75, 298, 304, 121, 314, 163, 36, 0, 146, 107, 116, 324, 228, 316, 85] ,
              [395, 121, 191, 214, 250, 69, 115, 145, 64, 247, 280, 286, 146, 0, 162, 289, 328, 324, 46, 151] ,
              [186, 230, 0, 87, 27, 334, 328, 353, 363, 124, 145, 109, 107, 162, 0, 346, 178, 43, 117, 114] ,
              [137, 4, 375, 124, 25, 216, 33, 71, 305, 206, 273, 122, 116, 289, 346, 0, 44, 175, 72, 44] ,
              [71, 351, 92, 234, 206, 270, 368, 119, 14, 320, 81, 339, 324, 328, 178, 44, 0, 327, 256, 78] ,
              [168, 230, 352, 122, 74, 208, 295, 130, 365, 281, 75, 333, 228, 324, 43, 175, 327, 0, 121, 182] ,
              [95, 286, 286, 81, 117, 130, 342, 40, 237, 157, 400, 50, 316, 46, 117, 72, 256, 121, 0, 321] ,
              [192, 84, 281, 107, 169, 177, 103, 268, 136, 289, 108, 16, 85, 151, 114, 44, 78, 182, 321, 0] ],
        'frm': 0,
        'to': 19,
        'length': 78,
        'path': 'brak przykladu'
    }
]


def print_graph(G):
    print("Graph:")
    print('[%s]' % ('\n '.join([str(row) for row in G])))
    

def runtests(f):
    ok = True
    for t in tests[:]:
      print_graph(t['G'])
      res = f(t['G'], t['frm'], t['to'])
      print('Actual length    : %s' % res)
      print('Expected length  : %s' % t['length'])
      print('Example path      : %s' % t['path'])
      if t['length'] == res:
        print('OK')
      else:
        print('Error') 
        ok = False
      print()
      #input()

    if ok: 
        print('Passed all tests')
    else:
        print('Failed')