class Node {
    constructor(key) {
        this.left = null;
        this.right = null;
        this.key = key;
    }
}

function newNode(key) {

    return new Node(key);
}

let v = 0;

function findLargestSumInTreeUtil(root) {

    if (root == null) {
        return 0;
    }

    let currSum = root.key + findLargestSumInTreeUtil(root.left) + findLargestSumInTreeUtil(root.right);

    console.log(currSum);

    v = Math.max(v, currSum)

    return currSum
}

// Function to find
// largest subtree sum.
function findLargestSubtreeSum(root) {
    // If tree does not exist,
    // then answer is 0.
    if (root == null)
        return 0;

    // Variable to store
    // maximum subtree sum.
    v = 0;

    // Call to recursive function
    // to find maximum subtree sum.
    findLargestSumInTreeUtil(root);

    return v;
}

/*
        1
        / \
        /     \
    -2     3
    / \     / \
    / \ / \
    4     5 -6     2
*/

let root = newNode(3);
root.left = newNode(7);
root.right = newNode(4);
root.left.left = newNode(2);
root.left.right = newNode(4);
root.right.left = newNode(4);
root.right.right = newNode(6);
root.left.left.left = newNode(8);
root.left.left.right = newNode(5);
root.left.right.left = newNode(5);
root.left.left.right = newNode(5);


console.log(findLargestSubtreeSum(root));