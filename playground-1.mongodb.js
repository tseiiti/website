

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

// por tipo
db.population.aggregate([
  { '$group': {
    '_id': { 'type': '$type' },
    'count': { '$sum': '$count' } }},
  { '$project': {
    '_id': 0,
    'type': '$_id.type',
    'count': 1, }},
  { '$sort' : {
    'type': -1 }},
]);

// por dia, cidade e tipo
db.population.aggregate([
  { '$group': {
    '_id': { 'city': '$city', 'type': '$type', 'date': '$date' },
    'count': { '$sum': '$count' } }},
  { '$project': {
    '_id': 0,
    'city': '$_id.city',
    'type': '$_id.type',
    'date': '$_id.date',
    'count': 1, }},
  { '$sort' : {
    'city' : 1, 'type': -1 }},
]);

db.population.aggregate([
  { '$project': {
    'city': 1,
    'count': 1,
    'date': { '$dateToString': { 'format': '%Y-%m', 'date': '$date' } },
    'ano': { '$dateToString': { 'format': '%Y', 'date': '$date' } },
    'mes': { '$dateToString': { 'format': '%m', 'date': '$date' } }, }},
  { '$group': {
    '_id': { 'city': '$city', 'type': '$type', 'date': '$date', 'ano': '$ano', 'mes': '$mes' },
    'count': { '$sum': '$count' } }},
  { '$project': {
    '_id': 0,
    'city': '$_id.city',
    'type': '$_id.type',
    'date': '$_id.date',
    'ano': '$_id.ano',
    'mes': '$_id.mes',
    'count': 1, }},
  { '$sort' : {
    'city' : 1, 'type': -1 }},
]);


