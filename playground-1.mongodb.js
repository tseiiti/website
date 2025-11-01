

// db.processes.aggregate([{
//   '$match': {
//     'cancels': { '$exists': true }
//   }}, {
//   '$project': {
//     '_id': 0,
//     'date': { '$dateToString': { 'format': '%Y-%m-%d', 'date': '$project_start' } },
//     'types': '$cancels.types.type.name',
//   }}, {
//   '$group': {
//     '_id': [ '$date', '$types' ],
//     'count': { '$sum': 1 }
//   }}, {
//   '$limit': 30
// }]);

db.population.find();

db.population.aggregate([
  { '$project': {
    'city': 1,
    'date': 1,
    'count': 1,
    'type': { '$cond': {
      'if': { '$regexMatch': { 'input': '$city', 'regex': 'total', 'options': 'i' } }, 'then': "Total",
      'else': "Cancelados" }}, }},
  { '$group': {
    '_id': { 'city': '$city', 'type': '$type', 'date': '$date' },
    'count': { '$sum': '$count' } }},
  { '$project': {
    '_id': 0,
    'city': { '$toUpper': { '$substrCP': [ '$_id.city', 0, 2 ] } },
    'type': '$_id.type',
    'date': '$_id.date',
    'count': 1, }},
  { '$sort' : {
    'city' : 1, 'type': 1 }},
]);

db.population.aggregate([
  { '$project': {
    'city': 1,
    'count': 1,
    'date': { '$dateToString': { 'format': '%Y-%m', 'date': '$date' } },
    'ano': { '$dateToString': { 'format': '%Y', 'date': '$date' } },
    'mes': { '$dateToString': { 'format': '%m', 'date': '$date' } },
    'type': { '$cond': {
      'if': { '$regexMatch': { 'input': '$city', 'regex': 'total', 'options': 'i' } }, 'then': "Total",
      'else': "Cancelados" }}, }},
  { '$group': {
    '_id': { 'city': '$city', 'type': '$type', 'date': '$date', 'ano': '$ano', 'mes': '$mes' },
    'count': { '$sum': '$count' } }},
  { '$project': {
    '_id': 0,
    'city': { '$toUpper': { '$substrCP': [ '$_id.city', 0, 2 ] } },
    'type': '$_id.type',
    'date': '$_id.date',
    'ano': '$_id.ano',
    'mes': '$_id.mes',
    'count': 1, }},
  { '$sort' : {
    'city' : 1, 'type': 1 }},
]);



// pip = [{
//   '$match': {
//      'cancels': { '$exists':True }
//   }}, {
//   '$project': {
//     '_id': 0,
//     'date': { '$dateToString': { 'format': '%Y-%m-%d', 'date': '$project_start' } },
//     'types': '$cancels.types.type.name',
//   }}, {
//   '$group': {
//     '_id': [ '$date', '$types' ],
//     'count': { '$sum': 1 }
//   }
//   }, {
//   '$limit': 3
// }]

// for e in col.aggregate(pip):
//   print(e)


// pip = [{ '$project': {'_id': 0, 'type': { '$cond': {'if': { '$regexMatch': { 'input': "$city", 'regex': '/total/i' } }, 'then': "Total",'else': "Cancelados" }}, 'city': 1, 'date': { '$dateToString': { 'format': '%Y-%m', 'date': '$date' } }, 'ano': { '$dateToString': { 'format': '%Y', 'date': '$date' } },'mes': { '$dateToString': { 'format': '%m', 'date': '$date' } },'count': 1, }},{ '$group': {'_id': { 'city': '$city', 'type': '$type', 'date': '$date', 'ano': '$ano', 'mes': '$mes' },'count': { '$sum': '$count' } }},{ '$project': {'_id': 0,'city': { '$toUpper': { '$substrCP': [ '$_id.city', 0, 2 ] } },'type': '$_id.type','date': '$_id.date','ano': '$_id.ano','mes': '$_id.mes','count': 1,}}]
// df = pd.DataFrame(col.aggregate(pip))
// pd.DataFrame(col.aggregate(pip)).query("type == 'Total'").pivot_table(index='date', columns='type', values='count', fill_value=0).astype(int)

// pip = [ { '$project': { '_id': 0, 'type': { '$cond': { 'if': { '$regexMatch': { 'input': "$city", 'regex': 'total', 'options': 'i' } }, 'then': "Total", 'else': "Cancelados" }}, 'city': 1, 'date': { '$dateToString': { 'format': '%Y-%m', 'date': '$date' } }, 'ano': { '$dateToString': { 'format': '%Y', 'date': '$date' } }, 'mes': { '$dateToString': { 'format': '%m', 'date': '$date' } }, 'count': 1, }}, { '$group': { '_id': { 'city': '$city', 'type': '$type', 'date': '$date', 'ano': '$ano', 'mes': '$mes' }, 'count': { '$sum': '$count' } }}, { '$project': { '_id': 0, 'city': { '$toUpper': { '$substrCP': [ '$_id.city', 0, 2 ] } }, 'type': '$_id.type', 'date': '$_id.date', 'ano': '$_id.ano', 'mes': '$_id.mes', 'count': 1, }} ]
// pd.DataFrame(col.aggregate(pip)).query("type == 'Total'")