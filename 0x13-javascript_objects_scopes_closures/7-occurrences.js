#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    list.reduce((count, current) => (current === searchElement ? count + 1 : count ), 0);
};