const fs = require('fs');
const { parse, printSchema } = require('graphql');
const AWS = require('aws-sdk');

const graphqlSchema = fs.readFileSync('data.graphql', 'utf8');

const schemaAST = parse(graphqlSchema);

const sdlSchema = printSchema(schemaAST);

const appSync = new AWS.AppSync();

const params = {
  apiId: 'oxqwkuucofbrvht3l2s4iskrte',
  definition: sdlSchema,
};

appSync.updateGraphqlApi(params, (err, data) => {
  if (err) console.error(err);
  else console.log('AppSync schema updated successfully');
});
